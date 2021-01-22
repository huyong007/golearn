Array.from(document.getElementsByTagName('table')[1].getElementsByClassName('cell el-tooltip')).filter(
    item => item.childNodes.length > 1
).map(item => item.innerText);