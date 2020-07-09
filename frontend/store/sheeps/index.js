export const state = () => ({
  sheeps: []
})

export const mutations = {
  loadSheeps(state, sheeps) {
    state.sheeps = sheeps
  }
}

export const actions = {
  async getSheeps({ commit }) {
    const sheeps = await this.$axios.$get('/api/v1/sheeps')
    commit('loadSheeps', sheeps)
  }
}
