const FOLDER_ID = "1_MXl-zkz6KEzqINMrTmUM52l2_aXQQnD";

function upload() {
    try {
        var folder = DriveApp.getFolderById(FOLDER_ID);
        var files = folder.getFiles();
        var fileArray = [];
        while (files.hasNext()) {
            fileArray.push(files.next());
        }

        if (fileArray.length === 0) {
            return ContentService.createTextOutput("Nenhum arquivo encontrado na pasta.");
        }

        var randomFile = fileArray[Math.floor(Math.random() * fileArray.length)];
        var videoBlob = randomFile.getBlob();

        var fileName = randomFile.getName();
        var title = fileName.replace(/\.[^/.]+$/, "");  // Remove a extensão do arquivo
        var tags = title.split(" ").map(function(tag) {
            return tag.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"");  // Remove caracteres especiais
        });

        var resource = {
            snippet: {
                title: title,
                description: title,
                tags: tags
            },
            status: {
                privacyStatus: "public",
            },
        };

        YouTube.Videos.insert(resource, "snippet,status", videoBlob);
      
        randomFile.setTrashed(true);
        Logger.log("Upload do vídeo concluído e arquivo deletado.");
        return ContentService.createTextOutput("Upload do vídeo concluído e arquivo deletado.")
    } catch (err) {
        Logger.log(err.message);
        return ContentService.createTextOutput(err.message);
    }
}
