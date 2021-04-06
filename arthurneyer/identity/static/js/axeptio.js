window.axeptioSettings = {
  clientId: "606c3e45669e094667543780",
  cookiesVersion: "zif-base",
};

(function(d, s) {
  var t = d.getElementsByTagName(s)[0], e = d.createElement(s);
  e.async = true; e.src = "https://static.axept.io/sdk.js";
  t.parentNode.insertBefore(e, t);
})(document, "script");

void 0 === window._axcb && (window._axcb = []);
window._axcb.push(function(axeptio) {
  axeptio.on("cookies:complete", function(choices) {

  })
})
