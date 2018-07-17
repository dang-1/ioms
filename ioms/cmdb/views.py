#coding: utf-8

import sys
import threading
import pymysql
import datetime
import multiprocessing

from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# from .serializers import HostSerializer

from .models import GsStatus, ZoneName, GsConfig

# db_config = settings.config_file
# with open(db_config, 'r') as f:
#     db_info = json.load(f)

db_password  = settings.CONFIG['gs_password']
# db_password = db_info['gs_db_passwod']

def get_sql():
    # time config
    now = datetime.datetime.now()
    now_before_1 = now - datetime.timedelta(1)
    now_before_2 = now - datetime.timedelta(2)
    now_before_7 = now - datetime.timedelta(7)
    now_before_15 = now - datetime.timedelta(15)
    now_before_30 = now - datetime.timedelta(30)

    # sql config
    sql1 = "select count(*) user_count from users;"
    sql2 = "select count(*) dau from player_track_statics \
            where track_date ='{}-{}-{}';".format(now_before_1.year, now_before_1.month, now_before_1.day)

    sql3 = "select count(DISTINCT open_udid) udid from player_track_statics \
            left join users on player_track_statics.user_id=users.id \
            where track_date='{}-{}-{}' and datediff(track_date,user_created_at)>0;".format(
        now.year, now.month, now.day)
    sql4 = "select distinct (case when c=0 then (select value from server_infos \
            where name='open_time') else (select date(updated_at) from server_infos \
            where name='merge_time') end) open_time from server_infos,(select count(name) c from server_infos \
            where name='merge_time')xx;"
    sql5 = "select sum(price)*0.7 revenue from orders \
            where is_validated='1' and created_at >'{}-{}-{}';".format(
        now_before_30.year, now_before_30.month, now_before_30.day)
    sql6 = "select count(distinct username) R from users inner join orders \
            on users.id=orders.user_id where users.last_login_day>'{}-{}-{}';".format(
        now_before_30.year, now_before_30.month, now_before_30.day)
    sql7 = "select COUNT(DISTINCT USER_ID) bigR from player_track_statics \
            where total_paid>='10000' and last_login_date>'{}-{}-{}';".format(
        now_before_30.year, now_before_30.month, now_before_30.day)
    sql8 = "select sum(sqrt((origin_soldier_atk_power/1000000)*(origin_soldier_def_power/1000000))) powerest_m from log_soldiers \
            where date(log_date)='{}-{}-{}' group by user_id order by powerest_m desc limit 1;".format(
        now_before_2.year, now_before_2.month, now_before_2.day)
    sql9 = "select avg(s) power_m from (select sum(sqrt(origin_soldier_atk_power/1000000*origin_soldier_def_power/1000000)) s \
            from log_soldiers where date(log_date)='{}-{}-{}' group by user_id)x ;".format(
        now_before_2.year, now_before_2.month, now_before_2.day)

    sql10 = "select sum(s) powerest_alliance_m from (select alliance_id, \
            sum(sqrt((origin_soldier_atk_power/1000000)*(origin_soldier_def_power/1000000))) s \
            from log_soldiers where date(log_date)='{}-{}-{}' group by user_id)x \
            where alliance_id>0 group by alliance_id order by powerest_alliance_m desc limit 1 ;".format(
        now_before_2.year, now_before_2.month, now_before_2.day)

    sql11 = "select avg(ss) power_alliance_m from (select sum(s) ss from \
            (select alliance_id,sum(sqrt((origin_soldier_atk_power/1000000)*(origin_soldier_def_power/1000000))) s \
            from log_soldiers where date(log_date)='{}-{}-{}' group by user_id)x \
            where alliance_id>0 group by alliance_id order by ss desc limit 10)xxxx ;".format(
        now_before_2.year, now_before_2.month, now_before_2.day)
    sql12 = "select sum(pvp)/7 pvp from player_track_dynamics where track_date between '{}-{}-{}' and '{}-{}-{}' ;".format(
        now_before_7.year, now_before_7.month, now_before_7.day, now_before_1.year, now_before_1.month,
        now_before_1.day)
    sql13 = "select avg(city_1_main_building_level_avg) level_1,avg(city_234_main_building_level_avg) \
            level_2,avg(city_5_main_building_level_avg) level_3 from users \
            inner join player_track_statics on users.id=player_track_statics.USER_id \
            where users.last_login_day>'{}-{}-{}' ;".format(
        now_before_15.year, now_before_15.month, now_before_15.day)
    # return [sql1, sql2, sql3, sql4, sql5, sql6, sql7, sql8, sql9, sql10, sql11, sql12, sql13]
    return [sql2, sql3, sql4, sql9]

class ConnMysql:
    def __init__(self, ip, port, user, password, char_set, database, sql_list):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.char_set = char_set
        self.database = database
        self.sql_list = sql_list
        self.return_data = {}
    def conn_mysql(self, sql):
        try:
            conn = pymysql.connect(host=self.ip, user=self.user, port=self.port, password=self.password, database=self.database)
            cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
            cur.execute(sql)
            data = cur.fetchall()
            print(data[0])
            self.return_data.update(data[0])
        except Exception as e:
            print("execute {} error in {} as {}".format(sql, self.ip, e))
            sys.exit(1)
        finally:
            conn.close()
    def run(self):
        for sql_one in self.sql_list:
            #t = threading.Thread(target=self.conn_mysql, args=(sql_one, ))
    	    #t.start()
    	    self.conn_mysql(sql_one)
        return self.return_data

# from .form import 
class GsStatusView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/gs_status.html'
    context_object_name = 'gs_status_list'
    model = GsStatus
    paginate_by = 30

    def get_context_data(self, **kwargs):
        # context = super(GsStatusView, self).get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: gs status page'
        return context


class ZoneNameView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/zone_name.html'
    context_object_name = 'zone_name_list'
    model = ZoneName

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: zone name page'
        return context


class GsListView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/gs_list.html'
    context_object_name = 'gs_config_list'
    model = GsConfig

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: gs config page'
        return context

    def post(self):
        return 'xxx'


class MergeListView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/merge_info.html'
    context_object_name = 'gs_list'
    queryset = GsConfig.objects.exclude(tag__tag_name='throne')
    # model = GsConfig

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: merge list info  page'
        return context

    def post(self):
        return 'xxx'

def update_all_merge_info(request):
    # all_gs_info = GsConfig.objects.filter(Q(gs_status__status=1), Q(tag__tag_name='ios_all') | Q(tag__tag_name='cn_all') | Q(tag__tag_name='ios_all'))
    all_gs_info = GsConfig.objects.all()
    procs = []
    for gs_one in all_gs_info:
        # try:
        #     gs_one = get_object_or_404(GsConfig, pk=)
        # except:
        #     print("get pk {} error".format(pk))
        #     redirect("cmdb:merge-info")
        print(gs_one.id)
        try:
            # db_ip = gs_one.gs_db.slave_host_info.outer_ip
            db_ip = gs_one.gs_db.slavedb.host_info.outer_ip
            db_port = gs_one.gs_db.slavedb.db_port
        except:
            db_ip = gs_one.gs_db.host_info.outer_ip
            db_port = gs_one.gs_db.db_port
        db_name = gs_one.gs_db_name

        proc = multiprocessing.Process(target=ConnMysql(db_ip, int(db_port), user, password, char_set, database, sql_list).run)
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()

        print(gs_one.gs_name, db_ip, db_port)
    return redirect("cmdb:merge-info")

def update_merge_info(request, pk):

    # print(pk)
    try:
        gs_one = get_object_or_404(GsConfig, pk=pk)
    except:
        print("get pk {} error".format(pk))
        redirect("cmdb:merge-info")
    try:
        # db_ip = gs_one.gs_db.slave_host_info.outer_ip
        db_ip = gs_one.gs_db.slavedb.host_info.outer_ip
        db_port = gs_one.gs_db.slavedb.db_port
    except:
        db_ip = gs_one.gs_db.host_info.outer_ip
        db_port = gs_one.gs_db.db_port
    db_name = gs_one.gs_db_name

    print(db_ip, db_port, db_name, db_password)

    # if db_ip.startswith('47'):
    #     db_user = 'db_analysis'
    #     # db_password =
    # else:
    #     db_user = 'x'
    #     # db_password = 'x'
    db_user = 'db_user'

    #ip, port, user, password, char_set, database, sql_list
    test_one = ConnMysql(db_ip, int(db_port), db_user, db_password, 'utf8', db_name, get_sql())
    data = test_one.run()

    try:
        # gs_one.big_r = data['bigR']
        gs.dau = data['dau']
        # gs.level = "{}-{}-{}".format(data['level_1'], data['level_2'], data['level_3'])
        # gs.power_alliance_m = data['power_alliance_m']
        # gs.powerest_alliance_m = data['powerest_alliance_m']
        # gs.powerest_m = data['powerest_m']
        # gs.pvp = data['pvp']
        # gs.R = data['R']
        # gs.revenue = data['revenue']
        gs.power_m = data['power_m']
        gs.udid = data['udid']
        gs.users = data['users']
        gs.save()
    except Exception as e:
        print("save {} error as {}".format(gs.id, e))
    redirect("cmdb:merge-info")

    # print(db_ip)


# class DbListView(LoginRequiredMixin, ListView):
#     template_name = 'cmdb/db_list.html'
#     context_object_name = 'db_list'
#     model =  DbConfig
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title_name'] = 'iomp: db config page'
#         return context



