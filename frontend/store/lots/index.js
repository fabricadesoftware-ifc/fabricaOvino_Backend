export const state = () => ({
  lots: []
})

export const mutations = {
  loadLots(state, lots) {
    state.lots = lots
  }
}

export const actions = {
  async getLots({ commit }) {
    const lots = await this.$axios.$get('/api/v1/lots')
    commit('loadLots', lots)
  }
}
