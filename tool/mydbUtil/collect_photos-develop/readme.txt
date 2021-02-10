
本工具用于  归纳整理 车检/查验 现场数据, 以供内部测试,训练使用。

详细内容 请查看：
 doc/
├── DEVELOP.txt
└── USEAGE.txt



ngx_http_geoip_module.so
ngx_http_image_filter_module.so
ngx_http_xslt_filter_module.so
ngx_mail_module.so  ngx_stream_module.so

apt-get install libxml2-dev
apt-get install libpcre3-dev
apt-get install php7.0-gd
apt-get install libxslt-dev

sudo ./configure --add-module=../../headers-more-nginx-module --with-stream --with-mail  --with-http_xslt_module  --with-http_geoip_module  --with-http_image_filter_module