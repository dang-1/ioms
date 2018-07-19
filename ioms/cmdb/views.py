#coding: utf-8

import sys
import threading
import pymysql
import datetime
import multiprocessing

from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.db.models import Q

from django.urls import reverse_lazy

from rest_framework import viewsets

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# from .serializers import HostSerializer
from .models import Tag, GsStatus, ZoneName, GsConfig
from .form import TagForm, GsStatusForm, ZoneNameForm, GsConfigForm

# config
db_password  = settings.CONFIG['gs_password']


#================================status begin==============================================
class GsStatusView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/gs_status_list.html'
    context_object_name = 'gs_status_list'
    model = GsStatus
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: gs status page'
        return context


# class GsDetailView(LoginRequiredMixin, DetailView):
#     template_name = "cmdb/gs_detail.html"
#     model = GsConfig
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title_name'] = 'iomp: cmdb gs detail page'
#         return context


class GsStatusUpdateView(LoginRequiredMixin, UpdateView):
    model = GsStatus
    fields = ['status', 'status_explain']
    template_name = 'union/update.html'
    success_url = reverse_lazy("cmdb:gs-status-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: cmdb tag update page'
        context['info'] = 'gs status'
        return context


class GsStatusAddView(LoginRequiredMixin, CreateView):
    model = GsStatus
    form_class = GsStatusForm
    template_name = "union/add.html"
    success_url = reverse_lazy("cmdb:gs-status-list")
    # success_url = "/cmdb/gs-status/list/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: tag add page'
        context['info'] = 'gs status'
        return context


class GsStatusDeleteView(LoginRequiredMixin, DeleteView):
    model = GsStatus
    fields = ['status', 'status_explain']
    template_name = 'union/delete.html'
    success_url = reverse_lazy("cmdb:gs-status-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: tag delete page'
        return context

#================================status end==============================================

#================================zonename begin==============================================

class ZoneNameView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/zone_name_list.html'
    context_object_name = 'zone_name_list'
    model = ZoneName

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: zone name page'
        return context


# class TagDetailView(LoginRequiredMixin, DetailView):
#     template_name = "cmdb/tag_detail.html"
#     model = Tag
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title_name'] = 'iomp: cmdb tag detail page'
#         return context
#
#
class ZoneNameUpdateView(LoginRequiredMixin, UpdateView):
    model = ZoneName
    fields = ['zone_name', 'zone_name_explain']
    template_name = 'union/update.html'
    success_url = reverse_lazy("cmdb:zone-name-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: zone name update page'
        return context


class ZoneNameAddView(LoginRequiredMixin, CreateView):
    model = ZoneName
    form_class = ZoneNameForm
    template_name = "union/add.html"
    success_url = reverse_lazy("cmdb:zone-name-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: zone name add page'
        context['info'] = 'zone name'
        return context


class ZoneNameDeleteView(LoginRequiredMixin, DeleteView):
    model = ZoneName
    fields = ['zone_name', 'zone_name_explain']
    template_name = 'union/delete.html'
    success_url = reverse_lazy("cmdb:zone-name-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: zone name delete page'
        return context
#================================zone name==============================================
#================================tag begin==============================================

class TagListView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/tag_list.html'
    context_object_name = 'tag_list'
    model = Tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: cmdb tag page'
        return context


class TagDetailView(LoginRequiredMixin, DetailView):
    template_name = "cmdb/tag_detail.html"
    model = Tag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: cmdb tag detail page'
        return context


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['tag_name', 'tag_explain']
    template_name = 'cmdb/tag_update.html'
    success_url = reverse_lazy("cmdb:tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: cmdb tag update page'
        return context


class TagAddView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = "cmdb/tag_add.html"
    success_url = reverse_lazy("cmdb:tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: tag add page'
        return context


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    fields = ['tag_name', 'tag_explain']
    template_name = 'cmdb/tag_delete.html'
    success_url = '/cmdb/tag/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: tag delete page'
        return context

#================================tag begin==============================================

#================================gs begin==============================================

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


class GsDetailView(LoginRequiredMixin, DetailView):
    template_name = "cmdb/gs_detail.html"
    model = GsConfig

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: cmdb gs detail page'
        return context


class GsUpdateView(LoginRequiredMixin, UpdateView):
    model = GsConfig
    fields = ['tag', 'gs_zone', 'gs_status', 'gs_accelerate_port']
    template_name = 'cmdb/gs_update.html'
    success_url = reverse_lazy("cmdb:gs-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: cmdb gs update page'
        return context


class GsAddView(LoginRequiredMixin, CreateView):
    model = GsConfig
    form_class = GsConfigForm
    template_name = "union/add.html"
    success_url = reverse_lazy("cmdb:gs-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'ioms: gs config add page'
        context['info'] = 'gs config'
        return context


# class TagDeleteView(LoginRequiredMixin, DeleteView):
#     model = Tag
#     fields = ['tag_name', 'tag_explain']
#     template_name = 'cmdb/tag_delete.html'
#     success_url = '/cmdb/tag/list/'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title_name'] = 'ioms: tag delete page'
#         return context

#================================gs end==============================================
#================================merge begin==============================================
def get_sql():
    '''return sql list'''
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
        now_before_1.year, now_before_1.month, now_before_1.day)
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
    return [sql1, sql2, sql3, sql4, sql9]

class ConnMysql:
    '''excute sql, return dict'''
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
            # sys.exit(1)
        finally:
            conn.close()
    def run(self):
        for sql_one in self.sql_list:
            #t = threading.Thread(target=self.conn_mysql, args=(sql_one, ))
    	    #t.start()
    	    self.conn_mysql(sql_one)
        return self.return_data


class MergeListView(LoginRequiredMixin, ListView):
    template_name = 'cmdb/merge_info.html'
    context_object_name = 'gs_list'
    # queryset = GsConfig.objects.exclude(tag__tag_name='throne')
    queryset = GsConfig.objects.filter(Q(gs_status__status=1), Q(tag__tag_name='an_all') | Q(tag__tag_name='cn_all') | Q(tag__tag_name='ios_all'))
    # model = GsConfig

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_name'] = 'iomp: merge list info  page'
        return context

    def post(self):
        return 'xxx'

def update_one_merge_info(id):
    try:
        gs_one = get_object_or_404(GsConfig, pk=id)
    except:
        print("get pk {} error".format(id))
        # redirect("cmdb:merge-info")
        return False
    try:
        db_ip = gs_one.gs_db.slavedb.host_info.outer_ip
        db_port = gs_one.gs_db.slavedb.db_port
    except:
        db_ip = gs_one.gs_db.host_info.outer_ip
        db_port = gs_one.gs_db.db_port
    db_name = gs_one.gs_db_name
    print(db_ip, db_port, db_name, db_password)
    db_user = 'db_user'
    #ip, port, user, password, char_set, database, sql_list
    test_one = ConnMysql(db_ip, int(db_port), db_user, db_password, 'utf8', db_name, get_sql())
    data = test_one.run()
    print(data)
    try:
        # gs_one.big_r = data['bigR']
        gs_one.dau = data['dau']
        # gs.level = "{}-{}-{}".format(data['level_1'], data['level_2'], data['level_3'])
        # gs.power_alliance_m = data['power_alliance_m']
        # gs.powerest_alliance_m = data['powerest_alliance_m']
        # gs.powerest_m = data['powerest_m']
        # gs.pvp = data['pvp']
        # gs.R = data['R']
        # gs.revenue = data['revenue']
        gs_one.power_m = data['power_m']
        gs_one.udid = data['udid']
        gs_one.users = data['user_count']

        try:
            if len(data['open_time']) == 10:
                gs_one.gs_open_time = datetime.datetime.strptime(data['open_time'], "%Y-%m-%d")
            elif len(data['open_time']) == 19:
                gs_one.gs_open_time = datetime.datetime.strptime(data['open_time'], "%Y-%m-%d %H:%M:%S")
            else:
                gs_one.gs_open_time = datetime.datetime.strptime(data['open_time'], '%a %b %d %H:%M:%S %Z %Y')
        except Exception as e:
            print("get {} open time error as {}".format(gs_one.gs_id, e))
        gs_one.save()
    except Exception as e:
        print("save {} error as {}".format(gs_one.id, e))
        return False
    # return redirect("cmdb:merge-info")


def update_all_merge_info(request):
    all_gs_info = GsConfig.objects.filter(Q(gs_status__status=1), Q(tag__tag_name='an_all') | Q(tag__tag_name='cn_all') | Q(tag__tag_name='ios_all'))
    # all_gs_info = GsConfig.objects.all()
    procs = []
    for gs_one in all_gs_info:
        # try:
        #     gs_one = get_object_or_404(GsConfig, pk=)
        # except:
        #     print("get pk {} error".format(pk))
        #     redirect("cmdb:merge-info")
        print(gs_one.id)
        # try:
        #     db_ip = gs_one.gs_db.slavedb.host_info.outer_ip
        #     db_port = gs_one.gs_db.slavedb.db_port
        # except:
        #     db_ip = gs_one.gs_db.host_info.outer_ip
        #     db_port = gs_one.gs_db.db_port
        # db_name = gs_one.gs_db_name

        # proc = multiprocessing.Process(target=ConnMysql(db_ip, int(db_port), user, password, char_set, database, sql_list).run)
        proc= multiprocessing.Process(target=update_one_merge_info, args=(gs_one.id,))
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
        db_ip = gs_one.gs_db.slavedb.host_info.outer_ip
        db_port = gs_one.gs_db.slavedb.db_port
    except:
        db_ip = gs_one.gs_db.host_info.outer_ip
        db_port = gs_one.gs_db.db_port
    db_name = gs_one.gs_db_name
    print(db_ip, db_port, db_name, db_password)
    db_user = 'db_user'
    #ip, port, user, password, char_set, database, sql_list
    test_one = ConnMysql(db_ip, int(db_port), db_user, db_password, 'utf8', db_name, get_sql())
    data = test_one.run()
    print(data)
    try:
        # gs_one.big_r = data['bigR']
        gs_one.dau = data['dau']
        # gs.level = "{}-{}-{}".format(data['level_1'], data['level_2'], data['level_3'])
        # gs.power_alliance_m = data['power_alliance_m']
        # gs.powerest_alliance_m = data['powerest_alliance_m']
        # gs.powerest_m = data['powerest_m']
        # gs.pvp = data['pvp']
        # gs.R = data['R']
        # gs.revenue = data['revenue']
        gs_one.power_m = data['power_m']
        gs_one.udid = data['udid']
        gs_one.users = data['user_count']

        try:
            if len(data['open_time']) == 10:
                gs_one.gs_open_time = datetime.datetime.strptime(data['open_time'], "%Y-%m-%d")
            elif len(data['open_time']) == 19:
                gs_one.gs_open_time = datetime.datetime.strptime(data['open_time'], "%Y-%m-%d %H:%M:%S")
            else:
                gs_one.gs_open_time = datetime.datetime.strptime(data['open_time'], '%a %b %d %H:%M:%S %Z %Y')
        except Exception as e:
            print("get {} open time error as {}".format(gs_one.gs_id, e))
        gs_one.save()
    except Exception as e:
        print("save {} error as {}".format(gs_one.id, e))
    return redirect("cmdb:merge-info")

#================================merge end==============================================
