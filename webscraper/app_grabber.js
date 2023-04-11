import { appendFileSync } from "fs";
import gplay from "google-play-scraper";

class App {
    constructor(title = "", developer="", privacyPolicy="") {
        this.title = title;
        this.developer = developer;
        this.privacyPolicy = privacyPolicy;
    }
    saveAsCSV() {
        const csv = `${this.title},${this.developer},${this.privacyPolicy}\n`;
        try {
            appendFileSync("./data.csv", csv);
        } catch (err) {
            console.error(err);
        }
    }
}

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
      
      results.forEach(test);
      
      function test(item) {
        var app = new App(item.title, item.developer, item.privacyPolicy);
        app.saveAsCSV();
      }
}

startApp();




