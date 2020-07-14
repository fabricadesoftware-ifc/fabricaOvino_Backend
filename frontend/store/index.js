export const state = () => ({})

export const actions = {
  async nuxtServerInit({ commit }) {
    try {
      const breeds = await this.$axios.$get('/api/v1/breeds')
      commit('breeds/loadBreeds', breeds)

      const categories = await this.$axios.$get('/api/v1/categories')
      commit('categories/loadCategories', categories)

      const sheeps = await this.$axios.$get('/api/v1/sheeps')
      commit('sheeps/loadSheeps', sheeps)
    } catch {
      console.log('not authenticated')
    }
  }
}
