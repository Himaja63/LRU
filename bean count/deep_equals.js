const deepEqual = function(obj1, obj2) {
    if (obj1 === obj2) {
      return true;
    } else if (isObject(obj1) && isObject(obj2)) {
      if (Object.keys(obj1).length !== Object.keys(obj2).length) { return false; }
      for (var prop in obj1) {
        if (!deepEqual(obj1[prop], obj2[prop])) {
          return false;
        }
      }
      return true;
    }
  
    // Private
  const isObject =  function(obj) {
      if (typeof obj === "object" && obj != null) {
        return true;
      } else {
        return false;
      }
    }
  }

  