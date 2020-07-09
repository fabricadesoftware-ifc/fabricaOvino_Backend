export const state = () => ({
  breeds: []
})

export const mutations = {
  loadBreeds(state, breeds) {
    state.breeds = breeds
  }
}

export const actions = {
  async getBreeds({ commit }) {
    const breeds = await this.$axios.$get('/api/v1/breeds')
    commit('loadBreeds', breeds)
  }
}
