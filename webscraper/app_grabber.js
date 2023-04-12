import gplay from "google-play-scraper";
import xlsx from 'xlsx';

const startApp = async () => {
    
    var result1 = (await gplay.list({
        category: gplay.category.FAMILY,
        num: 1000,
        fullDetail: true,
        throttle: 10
      }))

      var result2 = (await gplay.list({
        category: gplay.category.FAMILY,
        collection: gplay.collection.TOP_FREE,
        num: 1000,
        fullDetail: true,
        throttle: 10
      }))    
      
      var result3 = (await gplay.list({
        category: gplay.category.FAMILY,
        collection: gplay.collection.TOP_PAID,
        num: 1000,
        fullDetail: true,
        throttle: 10
      }))
      
      var result4 = (await gplay.list({
        category: gplay.category.FAMILY,
        collection: gplay.collection.GROSSING,
        num: 1000,
        fullDetail: true,
        throttle: 10
      }))

      var results = [...result1, ...result2, ...result3, ...result4]
      
      console.log(results.length)

      let binaryWS = xlsx.utils.json_to_sheet(results)

      var wb = xlsx.utils.book_new()

      xlsx.utils.book_append_sheet(wb, binaryWS, 'Binary values')

      xlsx.writeFile(wb, 'testData.xlsx');
}

startApp();




