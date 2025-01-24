sync: stations.json
	rsync -av --include="*/" --include="*19202030.csv" --exclude="*" ../../../../yamanashi-water/air/ ./data/
	rsync -av --include="*/" --include="*19206010.csv" --exclude="*" ../../../../yamanashi-water/air/ ./data/
	rsync -av --include="*/" --include="*19441030.csv" --exclude="*" ../../../../yamanashi-water/air/ ./data/
	rsync -av --include="*/" --include="*.txt" --exclude="*" ../../../../yamanashi-water/TD20231218_155555_51 ./data/

stations.json: ../../../../yamanashi-water/air/stations_loc.pickle Makefile pickle2json.py
	python pickle2json.py $< > $@