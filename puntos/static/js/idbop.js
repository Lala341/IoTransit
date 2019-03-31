var dbPromise = idb.open('puntos-db', 5, function(upgradeDb) {
	upgradeDb.createObjectStore('puntos',{keyPath:'pk'});
});


	//collect latest post from server and store in idb
	fetch('http://172.24.41.227:8082/getdata').then(function(response){
		return response.json();
	}).then(function(jsondata){
		dbPromise.then(function(db){
			var tx = db.transaction('puntos', 'readwrite');
	  		var feedsStore = tx.objectStore('puntos');
	  		for(var key in jsondata){
	  			if (jsondata.hasOwnProperty(key)) {
			    	feedsStore.put(jsondata[key]);
			  	}
	  		}
		});
	});

	//retrive data from idb and display on page
	var post="";
	dbPromise.then(function(db){
		var tx = db.transaction('puntos', 'readonly');
  		var feedsStore = tx.objectStore('puntos');
  		return feedsStore.openCursor();
	}).then(function logItems(cursor) {
		  if (!cursor) {
		  	document.getElementById('offlinedata').innerHTML=post;
		    return;
		  }
		  for (var field in cursor.value) {
		    	if(field=='fields'){
		    		feedsData=cursor.value[field];
		    		for(var key in feedsData){


		    			if(key =='nombre'){
		    				var title = '<h3>'+feedsData[key]+'</h3>';
		    			}
		    			if(key =='cantidad'){
		    				var author = feedsData[key];
		    			}
		    			if(key == 'tipo'){
		    				var body = '<p>'+feedsData[key]+'</p>';
		    			}
		    		}

		    		post=post+'<br>'+title+'<br>'+author+'<br>'+body+'<br>';
		    	}
		    }
		  return cursor.continue().then(logItems);
		});
