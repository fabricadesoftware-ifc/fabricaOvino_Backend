export const state = () => ({
  form: {
    newborns_quantity: 0,
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
  newbornEarringNumber(state, payload) {
    state.form.newborns[payload.index].earringNumber = payload.earringNumber
  },
  newbornWeight(state, payload) {
    state.form.newborns[payload.index].weight = payload.weight
  },
  newbornBreed(state, payload) {
    state.form.newborns[payload.index].breed = payload.breed
  },
  newbornCategory(state, payload) {
    state.form.newborns[payload.index].category = payload.category
  },
  newbornSex(state, payload) {
    state.form.newborns[payload.index].sex = payload.sex
  },
  addNewborns(state, payload) {
    state.form.newborns_quantity = payload.value
    let newNewborn = { sex: 'F' }
    state.form.newborns = state.form.newborns.concat(
      new Array(payload.diff).fill(newNewborn)
    )
  },
  removeNewborns(state, { value, diff }) {
    state.form.newborns.splice(
      state.form.newborns.length - diff,
      state.form.newborns.length
    ),
      (state.form.newborns_quantity = value)
  },
  reset(state) {
    state.form = {}
  }
}
