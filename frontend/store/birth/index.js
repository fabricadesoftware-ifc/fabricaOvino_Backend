export const state = () => ({
  form: {
    newbornsQuantity: 0,
    newborns: []
  }
})

export const mutations = {
  sheep(state, value) {
    state.form.sheep = value
  },
  date(state, value) {
    state.form.date = value
  },
  newbornName(state, payload) {
    state.form.newborns[payload.index].name = payload.name
  },
  newbornWeight(state, payload) {
    state.form.newborns[payload.index].weight = payload.weight
  },
  addNewborns(state, payload) {
    state.form.newbornsQuantity = payload.value
    let obj = {}
    state.form.newborns = state.form.newborns.concat(
      new Array(payload.diff).fill(obj)
    )
  },
  removeNewborns(state, { value, diff }) {
    state.form.newborns.splice(
      state.form.newborns.length - diff,
      state.form.newborns.length
    ),
      (state.form.newbornsQuantity = value)
  },
  reset(state) {
    state.form = {}
  }
}
