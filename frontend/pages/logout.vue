<template></template>

<script>
export default {
  async created() {
    await this.$auth.logout()
  }
}
</script>

