/*eslint-disable*/
export default function ({ app, store, $axios }) {
  $axios.onRequest(config => {
    console.log('Making request to ' + config.url + 'using ')
  })
  $axios.onResponseError(error => {
    // console.log(error)
    const code = parseInt(error.response && error.response.status)
    if (code === 401) {
      app
        .swal({
          type: 'warning',
          title: app.i18n.t('token_expired_alert_title'),
          text: app.i18n.t('token_expired_alert_text'),
          reverseButtons: true,
          confirmButtonText: app.i18n.t('ok'),
          cancelButtonText: app.i18n.t('cancel')
        })
        .then(() => {
          store.commit('auth/LOGOUT')
          console.log('test to redirectct')
          // redirect({
          //   name: 'homepage'
          // })
        })
    } else {
      console.log('aqui')
    }
  })
}
