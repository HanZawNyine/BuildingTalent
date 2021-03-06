var mySingleton = (function () { // Instance stores a reference to the Singleton
    var instance;

    function init() {

        // Singleton

        // Private methods and variables
        function privateMethod() {
            console.log("I am private");
        }

        var privateVariable = "Im also private";

        return { // Public methods and variables
            publicMethod: function () {
                console.log("The public can see me!");
            },

            publicProperty: "I am also public"
        };
    };
    return { // Get the Singleton instance if one exists// or create one if it doesn't
        getInstance: function () {
            if (! instance) {
                instance = init();
            }

            return instance;
        }

    };
})();

var singleA = mySingleton.getInstance();
var singleB = mySingleton.getInstance();
console.log(singleA === singleB); // true
