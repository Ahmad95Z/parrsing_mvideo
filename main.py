from pickle import FALSE
import requests
import json

def get_data():
    import requests

cookies = {
    '__lhash_': 'f8c026371319abd2736625a426a7450e',
    'COMPARISON_INDICATOR': 'false',
    'HINTS_FIO_COOKIE_NAME': '1',
    'MVID_AB_PDP_CHAR': '2',
    'MVID_AB_SERVICES_DESCRIPTION': 'var4',
    'MVID_AB_TOP_SERVICES': '0',
    'MVID_ADDRESS_COMMENT_AB_TEST': '2',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
    'MVID_CART_AVAILABILITY': 'true',
    'MVID_CART_MULTI_DELETE': 'true',
    'MVID_CATALOG_STATE': '1',
    'MVID_CITY_ID': 'CityDE_28082',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_GIFT_KIT': 'true',
    'MVID_GLC': 'true',
    'MVID_GUEST_ID': '21632776147',
    'MVID_HANDOVER_SUMMARY': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_KLADR_ID': '2000000100000',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_MCLICK': 'true',
    'MVID_MINDBOX_DYNAMICALLY': 'true',
    'MVID_MINI_PDP': 'true',
    'MVID_MOBILE_FILTERS': 'true',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_PROMO_CATALOG_ON': 'true',
    'MVID_REGION_ID': '62',
    'MVID_REGION_SHOP': 'S963',
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_WEBP_ENABLED': 'true',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'SENTRY_ERRORS_RATE': '0.1',
    'SENTRY_TRANSACTIONS_RATE': '0.5',
    'flacktory': 'no',
    'searchType2': '1',
    '_ym_uid': '166577696824477891',
    '_ym_d': '1665776968',
    '_sp_ses.d61c': '*',
    '_gid': 'GA1.2.1033456086.1665776968',
    '_ym_isad': '2',
    'partnerSrc': 'yandex',
    'admitad_uid': 'mvideo',
    'utm_term': 'mvideo',
    '__SourceTracker': 'yandex__cpc',
    'admitad_deduplication_cookie': 'yandex__cpc',
    '__cpatrack': 'yandex_cpc',
    '__sourceid': 'yandex',
    '__allsource': 'yandex',
    'SMSError': '',
    'authError': '',
    'tmr_lvid': '8244bb38baac62f3d02b8378948e7006',
    'tmr_lvidTS': '1665776970812',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': 'b5aed3b3-8d69-4089-9766-a061b3b1d867',
    'uxs_uid': '51ba7ef0-4bf9-11ed-b792-79610c30b981',
    'advcake_track_id': '066af6e3-6b7d-7a6a-e7a1-564fe24a1626',
    'advcake_session_id': '010b4fa1-9d4e-1804-57b3-aab2bd14d37e',
    'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3DIpr_RF_image_name_pure_broad_search%26utm_content%3Dpid%7C40621523240_%7Ccid%7C77542451%7Cgid%7C4998876029%7Caid%7C12579080345%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C1106%7Cregion_name%7C%25D0%2593%25D1%2580%25D0%25BE%25D0%25B7%25D0%25BD%25D1%258B%25D0%25B9%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3Dmvideo%26reff%3Dyandex_cpc_Ipr_RF_image_name_pure_broad_search%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs3NzU0MjQ1MTsxMjU3OTA4MDM0NTt5YW5kZXgucnU6cHJlbWl1bQ%26yclid%3D9161802120875212799',
    'advcake_utm_partner': 'Ipr_RF_image_name_pure_broad_search',
    'advcake_utm_webmaster': 'pid%7C40621523240_%7Ccid%7C77542451%7Cgid%7C4998876029%7Caid%7C12579080345%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C1106%7Cregion_name%7C%25D0%2593%25D1%2580%25D0%25BE%25D0%25B7%25D0%25BD%25D1%258B%25D0%25B9%7Ccoef_goal%7C0%7Cdesktop',
    'advcake_click_id': '',
    'flocktory-uuid': '261142e1-ebd3-4f2e-b4e8-38e94af87039-7',
    'afUserId': '358b0af2-b1da-4982-b0b0-63f62f92d808-p',
    'AF_SYNC': '1665776971763',
    'BIGipServeratg-ps-prod_tcp80': '1678040074.20480.0000',
    'bIPs': '389543560',
    'wurfl_device_id': 'generic_web_browser',
    'JSESSIONID': 'G2Q2jJ9PCcQ3Vq33KW8lgYphtdnTp2vS4rSMpVnQTG2fLhkG1xjk!1127004745',
    'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
    'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
    'BIGipServeratg-ps-prod_tcp80_clone': '1678040074.20480.0000',
    'MVID_GTM_BROWSER_THEME': '1',
    'deviceType': 'desktop',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VAPQ4fIWFiP1YQbnxLWhR6DkpXQ0IMfXk5L2dfLR8tal1hZnIVJ2M6NRZtWWs/RnI+ES82GjxmH2ZHWSNKWVJqJh8XfHIqVRASYD9HcGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeS5CbCNoTl8oRFtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=orCWFg==',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VAPQ4fIWFiP1YQbnxLWhR6DkpXQ0IMfXk5L2dfLR8tal1hZnIVJ2M6NRZtWWs/RnI+ES82GjxmH2ZHWSNKWVJqJh8XfHIqVRASYD9HcGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeS5CbCNoTl8oRFtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=orCWFg==',
    'cfidsgib-w-mvideo': 'Fdo2kHjl0RkMK51c7tvCkgC94oXwO05TSP3U8pGw/h1WrZEdKisG1g0EJVHzPl94ImWhnJuyF+/ekIWabfCPUMfFjLHW5xbtnYimvAtnGWrzQ0N1QjoZE6rPXJGR/XktHIq8OPILSP5YIAI3BTtyr+XpRHVebvQSYTgB',
    'cfidsgib-w-mvideo': 'Fdo2kHjl0RkMK51c7tvCkgC94oXwO05TSP3U8pGw/h1WrZEdKisG1g0EJVHzPl94ImWhnJuyF+/ekIWabfCPUMfFjLHW5xbtnYimvAtnGWrzQ0N1QjoZE6rPXJGR/XktHIq8OPILSP5YIAI3BTtyr+XpRHVebvQSYTgB',
    'gsscgib-w-mvideo': 'CLf4VNKjKVAnvh4cqyNEW1PwdsDHLxRkrNxGEjGug+EY4g7zvFwiujGhxu1rmN+PFSWdKQlom7dWJV6O0+biAMXY3pS05kXTmt8jbzezqojM/bxepKFAlQdqXnXhgPcBTaV5Hriv85bWtiUAy6ptO07Zl7THnj0g6qVPIDuVnA8hFzBd9LeOZpel7UD2GkDp2O2TzPjZSeG4n0MQtdNWZQcqEFMCwN9r+SxvsMaPXJYZJK3c2WkyeI3R/p978A==',
    'gsscgib-w-mvideo': 'CLf4VNKjKVAnvh4cqyNEW1PwdsDHLxRkrNxGEjGug+EY4g7zvFwiujGhxu1rmN+PFSWdKQlom7dWJV6O0+biAMXY3pS05kXTmt8jbzezqojM/bxepKFAlQdqXnXhgPcBTaV5Hriv85bWtiUAy6ptO07Zl7THnj0g6qVPIDuVnA8hFzBd9LeOZpel7UD2GkDp2O2TzPjZSeG4n0MQtdNWZQcqEFMCwN9r+SxvsMaPXJYZJK3c2WkyeI3R/p978A==',
    'fgsscgib-w-mvideo': 'MSgR064117e2c706a8339353be395f2c9b78d061',
    'fgsscgib-w-mvideo': 'MSgR064117e2c706a8339353be395f2c9b78d061',
    'cfidsgib-w-mvideo': '2jEjdUk8C6FfDdXgYDvOYhbksSxeS1xDbowN2h1lyDdoW0fhhYhJ/WMec6Tb/eI7JzGoXrGlsM0ZP2NyO1p8nHM5w2198gBhGI8Y6r7nNAlrG7ayF8YRnlUyge7WcwLFziO21+xhebkGyFVqHLfspgu0j655QvZhpnUp',
    'CACHE_INDICATOR': 'false',
    'MVID_ENVCLOUD': 'prod1',
    '_sp_id.d61c': 'b1b2fa58-7822-4c31-b3f1-24d39f19de14.1665776968.1.1665776992..f8aadb84-5d64-491b-a598-3d0d14fbc40b..ae531b56-2e87-40b9-a63f-9b9bcdd5eeb1.1665776967636.3',
    '_ga': 'GA1.2.4330160.1665776967',
    'tmr_detect': '0%7C1665776997595',
    'tmr_reqNum': '25',
    '_ga_CFMZTSS5FM': 'GS1.1.1665776967.1.1.1665777261.0.0.0',
    '_ga_BNX5WPP3YK': 'GS1.1.1665776967.1.1.1665777261.60.0.0',
}

headers = {
    'authority': 'www.mvideo.ru',
    'accept': 'application/json',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=9f82a7215840413fa8ee18c3090263f4,sentry-sample_rate=0%2C5',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__lhash_=f8c026371319abd2736625a426a7450e; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TOP_SERVICES=0; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityDE_28082; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GUEST_ID=21632776147; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=2000000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=62; MVID_REGION_SHOP=S963; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=1; _ym_uid=166577696824477891; _ym_d=1665776968; _sp_ses.d61c=*; _gid=GA1.2.1033456086.1665776968; _ym_isad=2; partnerSrc=yandex; admitad_uid=mvideo; utm_term=mvideo; __SourceTracker=yandex__cpc; admitad_deduplication_cookie=yandex__cpc; __cpatrack=yandex_cpc; __sourceid=yandex; __allsource=yandex; SMSError=; authError=; tmr_lvid=8244bb38baac62f3d02b8378948e7006; tmr_lvidTS=1665776970812; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=b5aed3b3-8d69-4089-9766-a061b3b1d867; uxs_uid=51ba7ef0-4bf9-11ed-b792-79610c30b981; advcake_track_id=066af6e3-6b7d-7a6a-e7a1-564fe24a1626; advcake_session_id=010b4fa1-9d4e-1804-57b3-aab2bd14d37e; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3DIpr_RF_image_name_pure_broad_search%26utm_content%3Dpid%7C40621523240_%7Ccid%7C77542451%7Cgid%7C4998876029%7Caid%7C12579080345%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C1106%7Cregion_name%7C%25D0%2593%25D1%2580%25D0%25BE%25D0%25B7%25D0%25BD%25D1%258B%25D0%25B9%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3Dmvideo%26reff%3Dyandex_cpc_Ipr_RF_image_name_pure_broad_search%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs3NzU0MjQ1MTsxMjU3OTA4MDM0NTt5YW5kZXgucnU6cHJlbWl1bQ%26yclid%3D9161802120875212799; advcake_utm_partner=Ipr_RF_image_name_pure_broad_search; advcake_utm_webmaster=pid%7C40621523240_%7Ccid%7C77542451%7Cgid%7C4998876029%7Caid%7C12579080345%7Cpos%7Cpremium1%7Ckey%7Cmvideo%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C1106%7Cregion_name%7C%25D0%2593%25D1%2580%25D0%25BE%25D0%25B7%25D0%25BD%25D1%258B%25D0%25B9%7Ccoef_goal%7C0%7Cdesktop; advcake_click_id=; flocktory-uuid=261142e1-ebd3-4f2e-b4e8-38e94af87039-7; afUserId=358b0af2-b1da-4982-b0b0-63f62f92d808-p; AF_SYNC=1665776971763; BIGipServeratg-ps-prod_tcp80=1678040074.20480.0000; bIPs=389543560; wurfl_device_id=generic_web_browser; JSESSIONID=G2Q2jJ9PCcQ3Vq33KW8lgYphtdnTp2vS4rSMpVnQTG2fLhkG1xjk!1127004745; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1678040074.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VAPQ4fIWFiP1YQbnxLWhR6DkpXQ0IMfXk5L2dfLR8tal1hZnIVJ2M6NRZtWWs/RnI+ES82GjxmH2ZHWSNKWVJqJh8XfHIqVRASYD9HcGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeS5CbCNoTl8oRFtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=orCWFg==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VAPQ4fIWFiP1YQbnxLWhR6DkpXQ0IMfXk5L2dfLR8tal1hZnIVJ2M6NRZtWWs/RnI+ES82GjxmH2ZHWSNKWVJqJh8XfHIqVRASYD9HcGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeS5CbCNoTl8oRFtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=orCWFg==; cfidsgib-w-mvideo=Fdo2kHjl0RkMK51c7tvCkgC94oXwO05TSP3U8pGw/h1WrZEdKisG1g0EJVHzPl94ImWhnJuyF+/ekIWabfCPUMfFjLHW5xbtnYimvAtnGWrzQ0N1QjoZE6rPXJGR/XktHIq8OPILSP5YIAI3BTtyr+XpRHVebvQSYTgB; cfidsgib-w-mvideo=Fdo2kHjl0RkMK51c7tvCkgC94oXwO05TSP3U8pGw/h1WrZEdKisG1g0EJVHzPl94ImWhnJuyF+/ekIWabfCPUMfFjLHW5xbtnYimvAtnGWrzQ0N1QjoZE6rPXJGR/XktHIq8OPILSP5YIAI3BTtyr+XpRHVebvQSYTgB; gsscgib-w-mvideo=CLf4VNKjKVAnvh4cqyNEW1PwdsDHLxRkrNxGEjGug+EY4g7zvFwiujGhxu1rmN+PFSWdKQlom7dWJV6O0+biAMXY3pS05kXTmt8jbzezqojM/bxepKFAlQdqXnXhgPcBTaV5Hriv85bWtiUAy6ptO07Zl7THnj0g6qVPIDuVnA8hFzBd9LeOZpel7UD2GkDp2O2TzPjZSeG4n0MQtdNWZQcqEFMCwN9r+SxvsMaPXJYZJK3c2WkyeI3R/p978A==; gsscgib-w-mvideo=CLf4VNKjKVAnvh4cqyNEW1PwdsDHLxRkrNxGEjGug+EY4g7zvFwiujGhxu1rmN+PFSWdKQlom7dWJV6O0+biAMXY3pS05kXTmt8jbzezqojM/bxepKFAlQdqXnXhgPcBTaV5Hriv85bWtiUAy6ptO07Zl7THnj0g6qVPIDuVnA8hFzBd9LeOZpel7UD2GkDp2O2TzPjZSeG4n0MQtdNWZQcqEFMCwN9r+SxvsMaPXJYZJK3c2WkyeI3R/p978A==; fgsscgib-w-mvideo=MSgR064117e2c706a8339353be395f2c9b78d061; fgsscgib-w-mvideo=MSgR064117e2c706a8339353be395f2c9b78d061; cfidsgib-w-mvideo=2jEjdUk8C6FfDdXgYDvOYhbksSxeS1xDbowN2h1lyDdoW0fhhYhJ/WMec6Tb/eI7JzGoXrGlsM0ZP2NyO1p8nHM5w2198gBhGI8Y6r7nNAlrG7ayF8YRnlUyge7WcwLFziO21+xhebkGyFVqHLfspgu0j655QvZhpnUp; CACHE_INDICATOR=false; MVID_ENVCLOUD=prod1; _sp_id.d61c=b1b2fa58-7822-4c31-b3f1-24d39f19de14.1665776968.1.1665776992..f8aadb84-5d64-491b-a598-3d0d14fbc40b..ae531b56-2e87-40b9-a63f-9b9bcdd5eeb1.1665776967636.3; _ga=GA1.2.4330160.1665776967; tmr_detect=0%7C1665776997595; tmr_reqNum=25; _ga_CFMZTSS5FM=GS1.1.1665776967.1.1.1665777261.0.0.0; _ga_BNX5WPP3YK=GS1.1.1665776967.1.1.1665777261.60.0.0',
    'referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914/tolko-v-nalichii=da/seriya-iphone=iphone-13-pro-max',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '9f82a7215840413fa8ee18c3090263f4-b4aa6c5d47f5d9e9-1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
    'x-set-application-id': '45e4b8fe-9a38-41de-b077-7a8c6c39435c',
}

params = {
    'categoryId': '205',
    'offset': '0',
    'limit': '24',
    'filterParams': [
        'WyJjYXRlZ29yeSIsIiIsImlwaG9uZS05MTQiXQ==',
        'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        'WyJzZXJpeWEtaXBob25lIiwiIiwiaXBob25lLTEzLXByby1tYXgiXQ==',
    ],
    'doTranslit': 'true',
}

response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()


products_id = response.get('body').get('products')
with open ('1_products_id.json', 'w') as file:
    json.dump(products_id,file, indent=4,ensure_ascii=False)

json_data = {
    'productIds': products_id,
    'mediaTypes': [
        'images',
    ],
    'category': True,
    'status': True,
    'brand': True,
    'propertyTypes': [
        'KEY',
    ],
    'propertiesConfig': {
        'propertiesPortionSize': 5,
    },
    'multioffer': False,
}

response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

with open ('2_items.json','w',) as file:
    json.dump(response,file,indent=4,ensure_ascii=False)

products_id_str = ','.join(products_id)

params = {
    'productIds': products_id_str,
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
}

response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
with open ('3_prices.json','w',) as file:
    json.dump(response,file,indent=4,ensure_ascii=False)

items_prices = {}
material_prices = response.get('body').get('materialPrices')
for item in material_prices:
    item_id = item.get('price').get('productId')
    item_base_price = item.get('price').get('basePrice')
    item_sale_price = item.get('price').get('salePrice')
    item_bonus = item.get('bonusRubles').get('total')

    items_prices[item_id] = {
        'item_basePrice' : item_base_price,
        'item_salePrice': item_sale_price,
        'item_bonus': item_bonus
         }
with open ('4_items_prices.json','w',) as file:
    json.dump(items_prices,file,indent=4,ensure_ascii=False)

def get_result():
    with open ('2_items.json') as file:
        products_data = json.load(file)
    with open ('4_items_prices.json') as file:
        products_price = json.load(file)
    products_data = products_data.get('body').get('products')

    for item in products_data:
        products_id = item.get('productId')
        if products_id in products_price:
            prices = products_price[products_id]
        
        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data,file,indent=4,ensure_ascii=False)

def main():
    get_data()
    get_result()

if __name__== '__main__':
    main()