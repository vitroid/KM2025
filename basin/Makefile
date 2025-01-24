sync: W05-08_14_GML W05-08_19_GML W12-52A-14-01.1_GML W12-52A-19-01.1_GML N03-20240101_14_GML N03-20240101_19_GML

W05-08_%_GML.zip:
	wget https://nlftp.mlit.go.jp/ksj/gml/data/W05/W05-08/W05-08_$*_GML.zip

W12-52A-%-01.1_GML.zip:
	wget https://nlftp.mlit.go.jp/ksj/gmlold/data/W12/W12-52A/W12-52A-$*-01.1_GML.zip

N03-20240101_%_GML.zip:
	wget https://nlftp.mlit.go.jp/ksj/gml/data/N03/N03-2024/N03-20240101_$*_GML.zip


# W12-52A-14-01.1_GML

%: %.zip
	mkdir $* && cd $* && unzip ../$*.zip

#https://nlftp.mlit.go.jp/ksj/gmlold/datalist/gmlold_KsjTmplt-W12.html

# <a class="waves-effect waves-light btn indigo btn_padding" id="menu-button" onclick="javascript:DownLd('0.91MB', 'W12-52A-04-01.1_GML.zip',  '../W12/W12-52A/W12-52A-04-01.1_GML.zip' ,this);">
# 									<span id="W12-52A-04-01.1_GML.zip-open" style="display: block">
# 										<i class="material-icons">file_download</i>
# 									</span>
# 									<span id="W12-52A-04-01.1_GML.zip-close" style="display: none">
# 										<i class="material-icons">star</i>
# 									</span>
# 								</a>

# <a class="waves-effect waves-light btn indigo btn_padding" id="menu-button" onclick="javascript:DownLd_new('20.4MB','N03-20240101_03_GML.zip','../N03/N03-2024/N03-20240101_03_GML.zip' ,this);">
#                                 <span id="N03-20240101_03_GML.zip-open_new" style="display: block">
#                                     <i class="material-icons">file_download</i>
#                                 </span>
#                                 <span id="N03-20240101_03_GML.zip-close_new" style="display: none">
#                                     <i class="material-icons">star</i>
#                                 </span>
#                             </a>