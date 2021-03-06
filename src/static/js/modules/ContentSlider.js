'use strict';

var $ = require( 'jquery' );
require( 'slick' );

/**
 * ContentSlider
 * @class
 *
 * @classdesc Slides content in and out of a container div.
 *
 * When an element inside container with class `content-show`
 * is clicked, the element matching its `data-content` value
 * will be cloned, inserted in a slide, and rotated into view in the
 * container, whose height will be recalculated to match new contents.
 * When elements with class `content-hide` are clicked,
 * the slide containing the element will be rotated out of view
 * and then removed from the DOM.
 *
 * @param {string} elem Container element.
 * @param {number} slideCount Number of permanent slides in the container.
 */
function ContentSlider( elem, slideCount ) {
  var self = this;
  this.$container = $( elem );
  this.speed = 300;
  this.slideCount = slideCount;

  // Initialize slick carousel.
  this.$container.slick( {
    dots:           false,
    infinite:       false,
    swipe:          false,
    speed:          this.speed,
    adaptiveHeight: true,
    arrows:         false,
    onBeforeChange: function( slider, currInd, targetInd ) {
      // When slide is changed, animate height of container to accommodate
      // new slide's height.
      var slide = slider.$slides[targetInd];
      slider.$slider.animate( { height: $( slide ).height() + 'px' }, self.speed );
    }
  } );
  this.slickObj = this.$container.getSlick();
  this.init();
}

ContentSlider.prototype.init = function() {
  // TODO: Remove this line when per-page JS is implemented.
  if ( !_isSlickAvailableOn( this ) ) return;

  var self = this;
  this.$container.height( $( this.slickObj.$slides[0] ).height() );
  this.$container.on( 'click.slider', '.content-show', $.proxy( this.slideInContent, this ) );
  this.$container.on( 'click.slider', '.content-hide', $.proxy( this.slideOutContent, this ) );
};

ContentSlider.prototype.slideInContent = function( e ) {
  e.preventDefault();
  var contents,
      self = this,
      $div = $( '<div>' ),
      $node = $( $( e.currentTarget ).data( 'content' ) );
  if ( $node.length ) {
    // TODO: Move content instead of cloning; use ids instead of classes.
    contents = $node.first().clone().show().appendTo( $div );
    this.$container.slickAdd( $div );
    this.$container.slickNext();
  }
};

ContentSlider.prototype.slideOutContent = function( e ) {
  var self = this;
  e.preventDefault();
  this.$container.slickPrev();

  // Once slide has been animated out of view, remove it from DOM.
  setTimeout( function() {
    self.$container.slickRemove( self.slickObj.$slides.length - 1 );
  }, this.speed );
};

ContentSlider.prototype.destroy = function() {
  // TODO: Remove this line when per-page JS is implemented.
  if ( !_isSlickAvailableOn( this ) ) return;

  // Remove all but permanent slides.
  while ( this.slickObj.$slides.length > this.slideCount ) {
    this.$container.slickRemove( this.slickObj.$slides.length - 1 );
  }

  // Remove listeners on container.
  this.$container.off( 'click.slider' );
  this.$container.unslick();
};

// TODO: This is used on at least `/the-bureau/bureau-structure/`,
// when page-specific JS is implemented the `this.slickObj` check for
// existence can be removed.
function _isSlickAvailableOn(target) {
  return target.slickObj === null ? false : true;
}

module.exports = ContentSlider;
