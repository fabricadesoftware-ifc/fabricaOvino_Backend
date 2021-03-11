export const state = () => ({
  shearing: []
})

export const mutations = {
  loadShearing(state, shearing) {
    state.shearing = shearing
  }
}

export const actions = {
  async getShearing({ commit }) {
    const shearing = await this.$axios.$get('/api/v1/shearing')
    commit('loadShearing', shearing)
  }
}
