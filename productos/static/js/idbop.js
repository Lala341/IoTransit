

var dbPromise = idb.open('productos-db', 1, function(upgradeDb) {
 upgradeDb.createObjectStore('productos',{keyPath:'pk'});
});

fetch('http://127.0.0.1:8000/getdata').then(function(response){
  return response.json();
 }).then(function(jsondata){
  dbPromise.then(function(db){
   var tx = db.transaction('productos', 'readwrite');
     var feedsStore = tx.objectStore('productos');
     for(var key in jsondata){
      if (jsondata.hasOwnProperty(key)) {
        feedsStore.put(jsondata[key]);
      }
     }
  });
 });
