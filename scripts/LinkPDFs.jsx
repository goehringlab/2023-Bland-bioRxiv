// Illustrator Script to Replace All Linked PNGs with PDFs

var doc = app.activeDocument;
var links = doc.placedItems;

// Loop through all linked items in the document
for (var i = 0; i < links.length; i++) {
    var linkedItem = links[i];

    // Check if the linked item is a PNG file
    if (linkedItem.file instanceof File && linkedItem.file.fullName.match(/\.png$/i)) {
        var fileName = linkedItem.file.name;
        var pdfFilePath = linkedItem.file.path + "/" + fileName.replace(".png", ".pdf");

        // Try to find the corresponding PDF file
        var pdfFile = new File(pdfFilePath);

        if (pdfFile.exists) {
            // Replace linked PNG with PDF
            linkedItem.file = pdfFile;
        } else {
            alert("PDF file not found for: " + fileName);
        }
    }
}

// If no PNGs are found, display a message
if (links.length === 0) {
    alert("No linked items found in the document.");
}
