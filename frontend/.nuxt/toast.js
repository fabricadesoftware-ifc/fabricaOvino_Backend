import Vue from 'vue'
import Toasted from 'vue-toasted'

Vue.use(Toasted, {"position":"top-center","iconPack":"fontawesome","duration":3000})

const globals = [{"name":"defaultSuccess","message":"Operação realizada com sucesso","options":{"type":"success","icon":"check"}}]
if(globals) {
  globals.forEach(global => {
    Vue.toasted.register(global.name, global.message, global.options)
  })
}

export default function (ctx, inject) {
  inject('toast', Vue.toasted)
}
