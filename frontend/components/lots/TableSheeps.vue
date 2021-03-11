<template>
  <b-tabs vertical>
    <b-tab-item label="Ovelhas" icon="sheep">
      <b-field grouped group-multiline>
        <div v-for="(column, index) in columns" :key="index">
          <b-checkbox v-model="column.visible">
            {{ column.label }}
          </b-checkbox>
        </div>
      </b-field>
      <b-table
        checkable
        striped
        :data="sheeps"
        paginated
        paginate-position="bottom"
        aria-next-label="Next page"
        aria-previous-label="Previous page"
        aria-page-label="Page"
        aria-current-label="Current page"
        per-page="10"
      >
        <template v-slot="props">
          <b-table-column
            v-for="(column, index) in columns"
            :key="index"
            :field="column.field"
            sortable
            :label="column.label"
            :visible="column.visible"
          >
            <span v-if="column.field == 'birthday'">
              {{ new Date(props.row[column.field]).toLocaleDateString() }}
            </span>
            <span v-if="column.field == 'sex'">
              <b-icon
                :icon="
                  props.row[column.field] === 'Male'
                    ? 'gender-male'
                    : 'gender-female'
                "
              >
              </b-icon>
              {{ props.row[column.field] }}
            </span>
            <span v-else>
              {{ props.row[column.field] }}
            </span>
          </b-table-column>
        </template>
        <template #bottom-left>
          <div class="buttons">
            <b-button type="is-primary" icon-left="plus-circle-outline">{{
              $t('buttons.add')
            }}</b-button>
            <b-button type="is-danger" icon-left="close-circle-outline">
              {{ $t('buttons.reset') }}
            </b-button>
          </div>
        </template>
      </b-table>
    </b-tab-item>
    <b-tab-item :label="$t('pages.lots.lot')" icon="view-grid">
      Mostrar as ovelhas inclusas no lote
    </b-tab-item>
  </b-tabs>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  data() {
    return {
      columns: [
        {
          field: 'earringNumber',
          label: this.$t('pages.admin.sheep.table.earringNumber'),
          visible: true
        },
        {
          field: 'breed',
          label: this.$t('pages.admin.sheep.table.breed'),
          visible: false
        },
        {
          field: 'category',
          label: this.$t('pages.admin.sheep.table.category'),
          visible: false
        },
        {
          field: 'sex',
          label: this.$t('pages.admin.sheep.table.sex'),
          visible: false
        },
        {
          field: 'birthday',
          label: this.$t('pages.admin.sheep.table.birthday'),
          visible: false
        }
      ]
    }
  },
  computed: {
    ...mapState('sheeps', ['sheeps'])
  },
  created() {
    this.getSheeps()
  },
  methods: {
    ...mapActions('sheeps', ['getSheeps'])
  }
}
</script>

<style></style>
