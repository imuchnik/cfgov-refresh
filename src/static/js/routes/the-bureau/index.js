/* ==========================================================================
   Bureau structure.
   Scripts for `/the-bureau/`.
   ========================================================================== */

'use strict';

var $ = require( 'jquery' );
require( 'slick' );

var BreakpointHandler = require( '../../modules/classes/BreakpointHandler' );
var MobileOnlyExpandable = require( '../../modules/classes/MobileOnlyExpandable' );

function init() {
  if ( $( 'html' ).hasClass( 'lt-ie9' ) ) {
    return;
  }

  // TODO: Remove this when per-page JS is introduced.
  if ( document.querySelectorAll( '.bureau-mission' ).length === 0 ) {
    return;
  }

  var bureauMissionDom = $( '.bureau-mission' );
  var handler = new BreakpointHandler( {
    breakpoint: 599,
    type:       'max',
    enter:      _enterBreakpoint,
    leave:      _leaveBreakpoint
  } );

  $( '.expandable__mobile-only' ).each( function() {
    handler = new MobileOnlyExpandable( $( this ), 599 );
  } );

  function _enterBreakpoint() {
    bureauMissionDom.slick( {
      dots: true
    } );
  }

  function _leaveBreakpoint() {
    bureauMissionDom.unslick();
  }
}

module.exports = { init: init };
