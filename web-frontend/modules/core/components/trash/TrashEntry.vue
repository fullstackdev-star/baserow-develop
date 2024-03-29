<template>
  <div
    ref="member"
    class="trash-entry"
    :class="{ 'trash-entry--disabled': disabled }"
  >
    <div class="trash-entry__initials">
      {{ trashEntry.user_who_trashed | nameAbbreviation }}
    </div>
    <div class="trash-entry__content">
      <div class="trash-entry__name">
        {{
          $t('trashEntry.name', {
            user: trashEntry.user_who_trashed || $t('trashEntry.deletedUser'),
            type: $t('trashType.' + trashEntry.trash_item_type),
            title: trashItemTitle,
            parent: trashEntry.parent_name
              ? $t('trashEntry.fromParent', { parent: trashEntry.parent_name })
              : '',
          })
        }}
      </div>
      <div class="trash-entry__deleted-at-display">{{ timeAgo }}</div>
      <span
        v-if="trashEntry.extra_description"
        class="trash-entry__extra-description"
      >
        {{ trashEntry.extra_description }}
      </span>
    </div>
    <div class="trash-entry__actions">
      <a
        v-if="!disabled"
        class="trash-entry__action"
        :class="{ 'trash-entry__action--loading': trashEntry.loading }"
        @click="emitRestoreIfNotLoading"
      >
        {{ trashEntry.loading ? '' : $t('trashEntry.restore') }}
      </a>
    </div>
  </div>
</template>

<script>
/**
 * Displays a specific TrashEntry with a link which will trigger the restoring of the
 * trashed entry. Shows extra information about the entry like it's name, who trashed it
 * , how long ago it was trashed etc.
 */
import moment from '@baserow/modules/core/moment'

export default {
  name: 'TrashEntry',
  props: {
    trashEntry: {
      type: Object,
      required: true,
    },
    disabled: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data() {
    return {}
  },
  computed: {
    timeAgo() {
      return moment.utc(this.trashEntry.trashed_at).fromNow()
    },
    trashItemTitle() {
      if (this.trashEntry.name === '') {
        return this.$t('trashEntry.unnamed', {
          type: this.$t('trashType.' + this.trashEntry.trash_item_type),
          id: this.trashEntry.trash_item_id,
        })
      } else {
        return this.trashEntry.name
      }
    },
  },
  methods: {
    emitRestoreIfNotLoading() {
      if (!this.trashEntry.loading) {
        this.$emit('restore', this.trashEntry)
      }
    },
  },
}
</script>
