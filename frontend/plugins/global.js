export const userKey = '__ovinos_systemuser '

export function showError(e) {
  for (var item in e.response.data) {
    this.$toast.error(item + ': ' + e.response.data[item])
  }
}

export default { showError, userKey }
