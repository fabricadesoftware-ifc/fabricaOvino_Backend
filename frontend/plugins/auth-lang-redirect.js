export default ({ app }) => {
  var redirect = app.$auth.$storage.options.redirect;
  for (var key in redirect) {
    redirect[key] = "/" + app.i18n.locale + redirect[key];
  }
  app.$auth.$storage.options.redirect = redirect;
};
