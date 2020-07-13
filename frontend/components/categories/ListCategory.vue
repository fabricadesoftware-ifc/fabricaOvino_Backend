<template>
  <b-table
    striped
    :data="categories"
    paginated
    paginate-position="bottom"
    aria-next-label="Next page"
    aria-previous-label="Previous page"
    aria-page-label="Page"
    aria-current-label="Current page"
    per-page="10"
  >
    <template slot-scope="props">
      <b-table-column
        v-for="(column, index) in columns"
        :key="index"
        :field="column.field"
        :sortable="column.sortable"
        :label="column.label"
      >
        {{ props.row[column.field] }}
      </b-table-column>

      <b-table-column
        field="actions"
        :label="$t('pages.admin.category.table.actions')"
      >
        <b-button
          type="is-warning"
          icon-left="pencil"
          @click="loadCategory(props.row)"
        >
        </b-button>
        <b-button
          type="is-danger"
          icon-left="trash-can-outline"
          @click="confirmRemove(props.row)"
        >
        </b-button>
      </b-table-column>
    </template>
  </b-table>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  data() {
    return {
      columns: [
        {
          field: 'id',
          label: this.$t('pages.admin.category.table.id'),
          sortable: true
        },
        {
          field: 'name',
          label: this.$t('pages.admin.category.table.name'),
          sortable: true
        }
      ]
    }
  },
  computed: {
    ...mapState('categories', ['categories'])
  },
  methods: {
    ...mapActions('categories', ['getCategories']),
    loadCategory(category) {
      this.$emit('loadCategory', category)
    },
    confirmRemove(category) {
      this.$buefy.dialog.confirm({
        title: 'Delete Category?',
        message:
          'Are you sure to <b>delete</b> this category? This action cannot be undone.',
        confirmText: 'Delete',
        cancelText: 'Cancel',
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () => this.remove(category)
      })
    },
    async remove(category) {
      const id = category.id
      const url = `/api/v1/categories/${id}`
      try {
        await this.$axios.delete(url)
        this.$toasted.global.defaultSuccess()
        this.getCategories()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    }
  },
  created() {
    this.getCategories()
  }
}
</script>

<style></style>
