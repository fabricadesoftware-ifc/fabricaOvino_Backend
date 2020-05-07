export const state = () => ({
  form: {
    newbornsQuantity: 0
  }
})

export const getters = {
  newbornsQuantity: state => state.form.newbornsQuantity
}

export const mutations = {
  sheep(state, value) {
    state.form.sheep = value
  },
  date(state, value) {
    state.form.date = value
  },
  newbornsQuantity(state, value) {
    state.form.newbornsQuantity = value
  },
  reset(state) {
    state.form = {}
  }
}
