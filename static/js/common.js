function setValue(eid, value) {
        if ('None' == value) {
            value = null
        }
        document.getElementById(eid).value = value;
}

function refillForm(param) {
//    param = JSON.parse(param)
    for (var key in param) {
      setValue(key, param[key])
    }
}