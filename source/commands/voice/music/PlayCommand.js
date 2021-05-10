const Command = require("../../Command");
const CommandTypeEnum = require("../../CommandTypeEnum");
const ytSearch = require("yt-search");
const validURL = require("../../../components/music/UrlChecker.js");
const getYouTubePlaylistId = require("../../../components/music/UrlPlaylist.js");
const { VoiceChannel, Message } = require("discord.js");

class PlayCommand extends Command {
    name = "play";
    description = "Joins and plays a video from youtube";
    usage =
        " *required:* <Youtube link> *or search terms:* <term1> <term2> <term3> ...";
    type = CommandTypeEnum.MUSIC;
    hasArguments = true;
    async execute(message, args, elia) {
        if (
            elia.dataComponent.getRadioMode() ||
            (elia.musicComponent.messageSenderInVoiceChannel(message) &&
                elia.musicComponent.messageSenderHasRightPermissions(message))
        ) {
            const voiceChannel = await elia.musicComponent.musicQueue.getVoiceChannel(
                message.member.voice.channel,
                message
            );
            if (validURL(args[0])) {
                this.playFromYouTube(voiceChannel, message);
            } else {
                this.searchAndPlayFromYouTube(
                    voiceChannel,
                    message,
                    args.join(" ")
                );
            }
        }
    }

    /**
     * Play's a video or playlist from YouTube
     *
     * @param {VoiceChannel} voiceChannel the VoiceChannel to join
     * @param {Message} message the message which requested the music
     */
    playFromYouTube(voiceChannel, message) {
        const id = getYouTubePlaylistId(args[0]);
        if (id != null)
            elia.musicComponent.musicQueue.playYouTubePlaylist(
                message,
                voiceChannel,
                id
            );
        else
            elia.musicComponent.musicQueue.playMusic(
                message,
                voiceChannel,
                args[0]
            );
    }

    /**
     * Searches a query in YouTube and then play's the first video result match, if result exits
     *
     * @param {VoiceChannel} voiceChannel the VoiceChannel to join
     * @param {Message} message the message which requested the music
     * @param {string} query the search terms in one string
     */
    searchAndPlayFromYouTube(voiceChannel, message, query) {
        const video = this.videoFinder(query);
        if (video) {
            elia.musicComponent.musicQueue.playMusic(
                message,
                voiceChannel,
                video.url,
                video.title
            );
        } else {
            elia.messageComponent.reply(message, "No video results found.");
        }
    }

    /**
     * Searches a srting on YouTube and get the fist result.
     *
     * @param {String} query the string to search on YouTube
     * @returns {?String} the first result of the query or null if no results
     */
    async videoFinder(query) {
        const videoResult = await ytSearch(query);
        return videoResult.videos.length > 1 ? videoResult.videos[0] : null;
    }
}

module.exports = PlayCommand;
