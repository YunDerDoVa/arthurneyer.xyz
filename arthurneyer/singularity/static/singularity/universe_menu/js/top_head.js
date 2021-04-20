
function create_singularity_universe_menu(menu) {
  if (menu == null) {
    var menu = document.createElement("nav");
    menu.id = "singularity_universe_menu";
    menu.classList.add('menu_space_digital');
  }

  var body = document.getElementById('singularity_body');
  body.appendChild(menu);

}
