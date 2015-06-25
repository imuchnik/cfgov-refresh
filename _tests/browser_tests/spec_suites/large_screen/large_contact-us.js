ContactUsPage = require( '../../page_objects/page_contact-us.js' );

describe( 'Beta Contact Page', function() {
  var page;

  beforeEach( function() {
    page = new ContactUsPage();
    page.get();
  } );

  it( 'should properly load in a browser', function() {
    expect( page.pageTitle() ).toBe( 'Contact us' );
  } );

  it( 'should include 48 individual offices in alpha order', function() {
    var firstOffice = page.offices.first().element( by.css( '.expandable_label' ) );
    var lastOffice = page.offices.last().element( by.css( '.expandable_label' ) );

    expect( page.offices.count() ).toEqual( 48 );
    expect( firstOffice.getText() ).toMatch( 'Academic Research Council' );
    expect( lastOffice.getText() ).toMatch( 'Your Money, Your Goals Toolkit' );
  } );
} );
