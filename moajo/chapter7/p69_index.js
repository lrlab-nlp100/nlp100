function search(){
    name = document.getElementById("name_textbox").value
    alias = document.getElementById("alias_textbox").value
    tag = document.getElementById("tag_textbox").value
    n="";
    a="";
    t="";
    if(name)n = "name="+name;
    if(alias)a = "alias="+alias;
    if(tag)t = "tag="+tag;

    q = [n,a,t].filter(a=>a.length!==0).join("&")
    if(q)q="?"+q;

    window.location.href = 'http://localhost:8000'+q;
}